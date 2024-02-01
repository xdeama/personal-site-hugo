if (navigator && navigator.clipboard) {
    addCopyButtons(navigator.clipboard);
} else {
//     Clipboard API is missing, so no copy buttons
}

function addCopyButtons(clipboard) {
    document.querySelectorAll('pre > code').forEach(function (codeBlock) {
        var pre = codeBlock.parentNode;
        if (pre.parentNode.classList.contains('highlight')) {
            var highlight = pre.parentNode;

            var button = document.createElement('button');
            button.className = 'copy-code-button';
            button.type = 'button';
            button.innerText = 'Copy';

            button.addEventListener('click', function () {
                clipboard.writeText(codeBlock.innerText).then(function () {
                    /* Chrome doesn't seem to blur automatically,
                       leaving the button in a focused state. */
                    button.blur();

                    button.innerText = 'Copied!';

                    setTimeout(function () {
                        button.innerText = 'Copy';
                    }, 2000);
                }, function (error) {
                    button.innerText = 'Error';
                });
            });

            highlight.parentNode.insertBefore(button, highlight.nextSibling);
        }
    });
}
