$(document).ready(function () {
	console.log("jquery works!");
	$("#employers-carousel").lightSlider({
        item: 2,
		loop: true,
		addClass: "employers-carousel",
		adaptiveHeight: true,
		keyPress: true,
		controls: true,
		prevHtml: '<i class="fas fa-chevron-left slider-control"></i>',
		nextHtml: '<i class="fas fa-chevron-right slider-control"></i>',
		onSliderLoad: function () {
			$("#employers-carousel").removeClass("cS-hidden");
		},
		responsive: [
			{
				breakpoint: 1200,
				settings: {
					item: 4,
					slideMove: 1,
					slideMargin: 6,
				},
			},
			{
				breakpoint: 568,
				settings: {
					item: 1,
					slideMove: 1,
                    slideMargin: 20,
				},
			},
		],
	});

    // $("#employers-carousel2").lightSlider({
    //     item: 1,
	// 	loop: true,
	// 	addClass: "employers-carousel",
	// 	adaptiveHeight: true,
	// 	keyPress: true,
	// 	controls: true,
	// 	prevHtml: '<i class="fas fa-chevron-left slider-control"></i>',
	// 	nextHtml: '<i class="fas fa-chevron-right slider-control"></i>',
	// 	onSliderLoad: function () {
	// 		$("#employers-carousel").removeClass("cS-hidden");
	// 	},
		
	// });
});



