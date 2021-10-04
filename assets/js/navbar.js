window.addEventListener('load', function () {
  const menuLabel = document.getElementById("menu-label");
  menuLabel.onclick = handleDropdownToggle;
})

function handleDropdownToggle(e) {
  const dropDownContent = document.getElementById("dropdown-content");
  const dropDownBox = document.getElementById("menu-icon");

  if(dropDownBox.checked) {
    dropDownContent.style.display = "none"; 
  } else {
    dropDownContent.style.display = "flex"; 
  }
}
