setTimeout(function name(params) {
    // code to change pics
    let pics = ['images/brush.jpg', 'images/mascara.jpg'];
    let div = document.getElementById('home_div');

    while (true) {
        let image_index = 0;
        // check if array end is reached
        if(image_index === pics.length){
            let image_index = 0;
            // change div background
            div.style.backgroundImage = url(pics[image_index]);
        }else{
            div.style.backgroundImage = url(pics[image_index])
        }

        image_index++;
    }

}, 5000);