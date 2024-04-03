const image = document.getElementById("image");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext('2d');
const downloadButton = document.getElementById('download');
const see = document.getElementById('see');

console.log(ctx);
canvas.width = image.width;
canvas.height = image.height;
var arr = [];
let drawing = false;
let x = 0;
let y = 0;

ctx.drawImage(image, 0, 0);

canvas.addEventListener('mousedown', (e)=>{
    drawing=true;
    x=e.offsetX;
    y=e.offsetY;
});

canvas.addEventListener('mouseup', ()=> drawing=false);

canvas.addEventListener('mouseout', ()=> drawing=false);

canvas.addEventListener('mousemove', (e)=>{
    if (drawing){
        arr.push([x, y]);
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(e.offsetX, e.offsetY);
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 5;
        ctx.stroke();
        x = e.offsetX;
        y = e.offsetY;
    }

});

download.addEventListener('click', () => {
    // Get the canvas data as an image URL
    const dataURL = canvas.toDataURL('image/png'); // Change format as needed (e.g., 'image/jpeg')
  
    // Create a temporary anchor element (link)
    const link = document.createElement('a');
    link.href = dataURL;
    link.download = 'carved_image.png'; // Change filename as needed
  
    // Simulate a click on the link to trigger download
    link.click();
  });

see.addEventListener('click', ()=>{console.log(arr);})