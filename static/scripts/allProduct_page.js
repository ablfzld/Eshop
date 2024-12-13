$("#ArchiveFilerBtn").click(function (e) { 
    if(ArchiveFilerBtn)
    {
        $(".archive-filter-groups-box").fadeIn();
        ArchiveFilerBtn = false;
    }
    else
    {
        $(".archive-filter-groups-box").fadeOut();
        ArchiveFilerBtn = true;
    }
});

function ChangePage(pageId) {
    $("#Current_Page").val(pageId);
    $("#Archive_Form").submit();
}