function convertDate(date){
    var dateParts = date.split(',');
    var year = parseInt(dateParts[1]);
    var month = dateParts[0].split(' ')[0].toLowerCase();
    var monthIndex = new Date().getMonth(month);
    var day = (parseInt(dateParts[0].split(' ')[1])>9)? dateParts[0].split(' ')[1]:"0"+dateParts[0].split(' ')[1];
    var mm = (parseInt(monthIndex)>9)? monthIndex:"0"+monthIndex;
    var new_date = year+"-"+mm+"-"+day ;

    return new_date;
}


$(document).ready(function(){
    $(".btn_update_transaction").click(function(){
        var form = $("#updateTransaction").find("form");
        var row = $(this).closest("tr");
        var transaction_date = convertDate(row.find("#date").text());

        form.find("#pk").val(row.find("#pk").text());
        form.find("#id_type").val(row.find("#type").text());
        form.find("#id_account").val(row.find("#account").text());
        form.find("#id_balance").val(row.find("#balance").text());
        form.find("#id_content").val(row.find("#content").text());
        //form.find("#transaction_date").val(transaction_date);
    });

    $(".btn_update_account").click(function(){
        var form = $("#updateAccount").find("form");
        var row = $(this).closest("#rowAccount");

        
        form.find("#pk").val(row.find("#pk").text());
        form.find("#name").val(row.find("#name").text());
        form.find("#phone").val(row.find("#phone").text());
        form.find("#allow_max").val(row.find("#allow_max").text());
        form.find("#type").val(row.find("#type").text());
        (row.find("#active").text() == 'نشط'||row.find("#active").text() == 'True')?form.find("#active").prop('checked',true) : form.find("#active").prop('checked',false);
    });
});


$(document).ready(function() {
    $(".btn_delete").click(function() {
        var tranId = $(this).data("tranId");
        var row = $(this).closest('tr');
        var div = row.find("div").html();
        row.find("div").html("");
        $("#delete-message").html(row.html());
        $("#delete_id").val(tranId);
        row.find("div").html(div);
    });
    $(".btn_delete_account").click(function() {
        var account_id = $(this).data("accountId");
        var row = $(this).closest('tr');
        var div = row.find("div").html();
        row.find("div").html("");
        $("#delete-account-message").html(row.html());
        $("#delete_account_id").val(account_id);
        row.find("div").html(div);
    });
});
