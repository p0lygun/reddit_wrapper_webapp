const PRODUCTION_HOSTNAME = 'probe-reddit.vibhakar.dev',
    PRODUCTION_API_HOST = `probe-reddit-api.vibhakar.dev`,
    DEBUG = !(window.location.hostname === PRODUCTION_HOSTNAME);
let inputTimeout = null;
(function setupSubredditNameInput(){
    console.log('Initializing subreddit name input')
    function subredditNameInputHandler(event) {
        if (inputTimeout) {
            clearTimeout(inputTimeout);
        }
        const new_length = event.target.value.length;
        if (new_length===0) {
            event.target.setAttribute('size', "15");
        } else {
            event.target.setAttribute('size', new_length);
            inputTimeout = setTimeout(() => {
                getSubredditPosts();
            }
            , 1000);
        }
    }

    let subredditNameInput = document.getElementById('subreddit-name-input');
    subredditNameInput.setAttribute('size', "15");
    subredditNameInput.addEventListener('input', subredditNameInputHandler);
})();

function getSubredditPosts() {
    const subredditNameInput = document.getElementById('subreddit-name-input'),
        subredditName = subredditNameInput.value,
        pageDivider = document.querySelectorAll('.page-divider');

    console.debug('getSubredditPosts', subredditName)
    let API_HOST
    if (DEBUG)
        API_HOST = 'http://0.0.0.0:8787'
    else
        API_HOST = `https://${PRODUCTION_API_HOST}`

    const API_URL = `${API_HOST}/reddit/subreddit/${subredditName}?limit=12`;


    subredditNameInput.disabled = true;
    pageDivider.forEach(div => {
        div.classList.add('bg-orange-400')
    })
    const resp_json = fetch(API_URL).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            console.log(`Error fetching ${subredditName} posts`)
            return response.json();
        }
    }).finally(() => {
        subredditNameInput.disabled = false;
        subredditNameInput.focus();
    });

    resp_json.then(json => {
        processApiResponse(json)
    })
}

function processApiResponse(json) {
    console.debug('populateSubredditPosts', json)
    const pageDivider = document.querySelectorAll('.page-divider'),
        errorDiv = document.getElementById('api-response-error');
    pageDivider.forEach(div => {
        div.classList.remove('bg-orange-400')
    })
    if(json.hasOwnProperty('detail')){
        pageDivider.forEach(div => {
            div.classList.add('bg-fg-accent')
        })

        if (json.detail.hasOwnProperty('reason'))
            errorDiv.innerText = `Unable to get posts because subreddit is ${json.detail.reason}`;
        else
            errorDiv.innerText = `${json.detail.message}`;
    } else {
        // todo: show posts
        pageDivider.forEach(div => {
            div.classList.add('bg-green-400')
        })
        errorDiv.innerText = '';

        const injectionDiv = document.getElementById('posts');
        if(json.hasOwnProperty('posts')){
            injectionDiv.innerHTML = ''
            json.posts.forEach(post_json => {
                if(post_json.valid){
                    const creation_date = new Date(post_json.created_utc * 1000)
                    injectionDiv.innerHTML += `
                            <a href="${post_json.link}" target="_blank" class="w-full">
                                <div class="post w-full min-h-[9rem] flex flex-col gap-y-2 bg-bg-accent rounded-md p-2 transition duration-300 ease-in-out hover:-translate-y-2 md:min-h-fit">
                                    <div class="flex flex-row items-baseline gap-x-2 flex-wrap">
                                        <p class="text-fg text-sm">By</p>
                                        <p class="text-white ">u/${post_json.author}</p>
                                        <p class="text-fg text-sm">${getRelativeTimeString(creation_date, navigator.language)}</p>
                                    </div>
                                    <div class="text-lg text-ellipsis text-white">${post_json.title}</div>
                                </div>
                            </a>
                    `
                }
            })
        }
    }

    setTimeout(() => {
        pageDivider.forEach(div => {
            div.classList.remove('bg-fg-accent')
            div.classList.remove('bg-green-400')
        })
    }, 1000);
}

/**
 * Convert a date to a relative time string, such as
 * "a minute ago", "in 2 hours", "yesterday", "3 months ago", etc.
 * using Intl.RelativeTimeFormat
 */
function getRelativeTimeString(date, lang) {
    if (lang === void 0) { lang = "en"; }
    const timeMs = typeof date === "number" ? date : date.getTime();
    const deltaSeconds = Math.round((timeMs - Date.now()) / 1000);
    const cutoffs = [60, 3600, 86400, 86400 * 7, 86400 * 30, 86400 * 365, Infinity];
    const units = ["second", "minute", "hour", "day", "week", "month", "year"];
    const unitIndex = cutoffs.findIndex(function (cutoff) {
        return cutoff > Math.abs(deltaSeconds);
    });
    const divisor = unitIndex ? cutoffs[unitIndex - 1] : 1;
    const rtf = new Intl.RelativeTimeFormat(lang, {numeric: "auto"});
    return rtf.format(Math.floor(deltaSeconds / divisor), units[unitIndex]);
}
