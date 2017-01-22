/// <reference path="jquery-vsdoc.js" />

$(document).ready(function () {
    $("div[id^=tabs]").each(function () {
        $(this).tabs({ cookie: { expires: 30} });
    });
});