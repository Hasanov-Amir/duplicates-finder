function toggleRow(rowNumber) {
    var row = document.getElementsByClassName("row")[rowNumber - 1];
    var content = row.getElementsByClassName("row-content")[0];
    var arrow = row.getElementsByClassName("arrow")[0];

    if (content.style.display === "none") {
        content.style.display = "block";
        row.style.backgroundColor = "white";
        arrow.classList.add("arrow-down");
    } else {
        content.style.display = "none";
        row.style.backgroundColor = "lightgray";
        arrow.classList.remove("arrow-down");
    }
}