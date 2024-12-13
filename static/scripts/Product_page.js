$(document).ready(function () {
    $("#ReplyAlert").fadeOut(1);

});

function LikeArticle(p_id, u_id) {
    //TODO Send Data

    //TODO Show alert

}

function SaveArticle(p_id, u_id) {
    //TODO Send Data to server
    //TODO Show alert

}

function ReplyComment(c_id, u_name) {
    $("#CommentParentId").val(c_id);
    window.location.href = "#Replay_place";
    $("#ReplyAlertName").text(u_name);
    $("#ReplyAlert").fadeIn();
}

function CancleReply() {
    $("#CommentParentId").val(0);
    $("#ReplyAlert").fadeOut();
}

function AddComment() {
    let article_id = $("#ArtilceId").val();
    let parent_id = $("#CommentParentId").val();
    let text = $("#CommentText").val();

    //TODO Send Request To Server

    if (parent_id == 0) {
        let comment_box = `
            <!-- comment box -->
            <li class="comments-box">
                <header>
                    <img src="/static/imgs/user.png" />
                    <h5>کاربر</h5>
                    <button class="comments-box-reply" onclick="ReplyComment(1,'test1')">جواب</button>
                    <button class="comments-box-remove" onclick="RemoveComment(1)">حذف</button>
                </header>
                <p>`+ text + `</p>
                <span>2023/11/16</span>
            </li>
            <!-- comment box --> `;
        document.getElementById('CommentsList').innerHTML = comment_box + document.getElementById('CommentsList').innerHTML;
    }
    else {
        let comment_box = `
                <!-- comment box -->
                <li class="comments-box comments-answare">
                    <header>
                        <img src="/static/imgs/user.png" />
                        <h5>user_name</h5>
                        <button class="comments-box-remove" onclick="RemoveComment(1)">Delete</button>
                    </header>
                    <p>`+ text + `</p>
                    <span>2023/11/16</span>
                </li>
                <!-- comment box --> `;
        document.getElementById('Comment_' + parent_id).innerHTML += comment_box;
    }

    CancleReply();
    $("#CommentText").val('');
    //TODO Show alert
}

function RemoveComment(c_id) {
    //TODO Ask question 

    //TODO Request to srver
    $("#Comment_" + c_id).fadeOut();
    //TODO Show alert

}