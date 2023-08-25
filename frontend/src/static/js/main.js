(function setupSubredditNameInput(){
    console.log('Initializing subreddit name input')
    function subredditNameInputHandler(event) {
        console.log('subredditNameInputHandler', event.target.value.length)
        const new_length = event.target.value.length;
        if (new_length===0) {
            event.target.setAttribute('size', "15");
        } else {
            event.target.setAttribute('size', new_length);
        }
    }

    let subredditNameInput = document.getElementById('subreddit-name-input');
    subredditNameInput.setAttribute('size', "15");
    subredditNameInput.addEventListener('input', subredditNameInputHandler);
})();
