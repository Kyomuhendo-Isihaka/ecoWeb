// Loading the  rooms details page to main div
$(document).ready(function () {
	$(".add_room").click(function(){
		$(".main").load("addRoom.html");
	});
    $(".customers_details").click(function(){
		$(".main").load("customers.html");
	});
    $(".food").click(function(){
		$(".main").load("addFood.html");
	});

    $(".views").click(function(){
		$(".main").load("views.html");
	});

});

// Loading the customers details page to main div
// $(document).ready(function () {
	
// });

// // Loading the services details page to main div
// $(function () {
	
// });

// // Loading views for deleting contents
// $(function () {
// 	$(".views").click(function () {
// 		$(".main").load("views.html");
// 	});
// });
