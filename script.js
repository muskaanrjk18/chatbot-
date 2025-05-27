document.getElementById("no").addEventListener("click", function() {
    document.getElementById("response").innerText = "Forgiveness does not change the past, but it does enlarge the future.I love you! ❤️🌹";
    
});

document.getElementById("yes").addEventListener("mouseover", function() {
    this.style.position = "absolute";
    this.style.top = Math.random() * window.innerHeight + "px";
    this.style.left = Math.random() * window.innerWidth + "px";
});
