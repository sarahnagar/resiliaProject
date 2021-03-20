// When notification button is clicked, get the data from the API
$(document).ready(function () {
    $('#getNotifications').click(function () {
    $.ajax({
            type: 'GET',
            url: 'http://localhost:8080/notifications',
            dataType: "json",
            success: function (data) {
                console.log('success');
                console.log(data)
                cardNotification(data);
            }
        });

    });
});
// If the notifications are open, then close it and vice versa
function methodToCall(){
    if (document.getElementById("openNotifications").style.display == "none") {
      document.getElementById("openNotifications").style.display = "block";
    } else {
      document.getElementById("openNotifications").style.display = "none";
    }
}
// When user clicks inside the element, keep the element open, otherwise close it
document.addEventListener("click", (evt) => {
        const notificationButton = document.getElementById("getNotifications");
        const showingNotifications = document.getElementById("openNotifications");
        let targetEl = evt.target; // clicked element
        do {
          if(targetEl == notificationButton) {
            return methodToCall();
          }
          if(targetEl == showingNotifications) {
            return document.getElementById("openNotifications").style.display = "block";
          }
          targetEl = targetEl.parentNode;
        } while (targetEl);
            return document.getElementById("openNotifications").style.display = "none";
      });

// Setting the card's display style back to none
// so the next time the button is clicked it will open
$('.close').click(function(){
    var card = document.getElementById("openNotifications");
    card.style.display = "none";  // <-- Set it to block

})
// Create cards with notification data
let cardNotification = function (data) {
    $('#populateCards').html('');
    data.forEach(function (item) {
    console.log(item);
    $('#populateCards').append(
    '<div>' +
        '<div>' +
        '<h6 class="card-title" style="font-size:15px">' + item.division +'</h6>' +
        '</div>'+
        '<div>' +
        '<h6 class="card-subtitle mb-2 text-muted" style="font-size:10px">' + new Date(item.timestamp) +
        '</h6>' +
         '</div>' +
         '<h6 class="card-text" style="font-size:12px">' + item.notification + '</h6>'+
         '<hr border-top: 1px solid #8c8b8b>' +
         '</div>'
    );
});
};