document.addEventListener("DOMContentLoaded", function() {
    const tocList = document.getElementById('tocList');
    const headers = document.querySelectorAll('.blog-post-content h1, .blog-post-content h2, .blog-post-content h3, .blog-post-content h4, .blog-post-content h5, .blog-post-content h6');

    headers.forEach((header, index) => {
        const id = `heading-${index}`;
        header.id = id;

        const listItem = document.createElement('li');
        const link = document.createElement('a');

        link.href = `#${id}`;
        link.innerText = header.innerText;

        listItem.appendChild(link);
        tocList.appendChild(listItem);
    });
});
