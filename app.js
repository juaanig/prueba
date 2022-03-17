var card = `
        <div class="card">
            <h2 class="title-card">TITULO</h2>
            <div class="card-content">
                <img src="space.jpg" alt="">
                <p class="p-card">Lorem ipsum dolor sit amet consectetur adipisicing elit. Error quos enim animi id sequi numquam expedita nulla, ut voluptatibus incidunt deleniti laborum maiores, culpa et officiis magnam, reprehenderit sit at.</p>
            </div>
        </div> 
        `

function adder(){
    for(let i = 0 ;i < 4; i++){
        const $container = document.getElementById('container');
        $container.innerHTML += card;
    }
}


   




