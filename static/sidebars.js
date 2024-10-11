/* global bootstrap: false */
(() => {
  'use strict'
  const tooltipTriggerList = Array.from(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.forEach(tooltipTriggerEl => {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})()


//document.addEventListener("DOMContentLoaded", function() {
//    var collapseElement = document.getElementById("home-collapse");
//    var toggleButton = document.getElementById("toggle-button");
//
//    // 페이지가 로드될 때 저장된 상태를 복원
//    var savedState = localStorage.getItem("home-collapse-state");
//
//    if (savedState === "show") {
//        collapseElement.classList.add("show");
//    } else {
//        collapseElement.classList.remove("show");
//    }
//
//    // 버튼 클릭 시 show 클래스 토글
//    toggleButton.addEventListener("click", function() {
//        collapseElement.classList.toggle("show");
//
//        // 상태를 저장
//        if (collapseElement.classList.contains("show")) {
//            localStorage.setItem("home-collapse-state", "show");
//        } else {
//            localStorage.setItem("home-collapse-state", "hide");
//        }
//    });
//});