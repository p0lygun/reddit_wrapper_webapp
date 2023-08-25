let inputTimeout = null;
(function setupSubredditNameInput(){
    console.log('Initializing subreddit name input')
    function subredditNameInputHandler(event) {
        const new_length = event.target.value.length;
        if (new_length===0) {
            event.target.setAttribute('size', "15");
        } else {
            event.target.setAttribute('size', new_length);
            if (inputTimeout) {
                clearTimeout(inputTimeout);
            }
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
        pageDivider = document.getElementById('page-divider');

    console.debug('getSubredditPosts', subredditName)
    const DEBUG = true;
    let API_HOST
    if (DEBUG)
        API_HOST = 'http://0.0.0.0:8787'
    else
        API_HOST = 'https://reddit.stillearning.com'

    const API_URL = `${API_HOST}/reddit/subreddit/${subredditName}`;


    subredditNameInput.disabled = true;
    pageDivider.classList.add('bg-orange-400')
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
    const pageDivider = document.getElementById('page-divider');
    if(json.hasOwnProperty('detail')){
        // API returned an error
        pageDivider.classList.remove('bg-orange-400')
        pageDivider.classList.add('bg-fg-accent')
        // todo: show error message
    } else {
        // todo: show posts
    }

    setTimeout(() => {
        pageDivider.classList.remove('bg-fg-accent')
    }, 2000);
}
