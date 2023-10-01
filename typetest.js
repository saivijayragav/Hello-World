const paragraphs = [
    "Amidst a field of wildflowers, the sun kissed the petals, igniting a riot of colors. Bees hummed a lively tune as they darted from bloom to bloom, gathering nature's sweet nectar. Soft breezes whispered secrets through the grass, carrying the scents of earth and blossoms. Butterflies danced on fragile wings, their delicate beauty captivating the eyes. In this vibrant tapestry of life, nature's symphony played on, a harmonious blend of sights, scents, and sounds.",
    "A winding path led through a mystical forest, where ancient trees stood tall, their gnarled branches reaching for the heavens. Sunlight filtered through the leafy canopy, casting enchanting patterns on the forest floor. The air was thick with earthy fragrances, hinting at the hidden wonders within. Moss-covered rocks dotted the landscape, inviting weary travelers to rest and ponder the mysteries of the woods. Here, time stood still, and the veil between reality and fantasy grew thin.",
    "Nestled on a mountainside, a cascading waterfall spilled its crystal-clear waters into a pristine pool below. The rush of the falls created a symphony of nature, mingling with the chirping of birds and the rustling of leaves. Sunlight danced on the spray, creating a prism of colors that painted the surroundings with ethereal beauty. Surrounded by towering peaks, this sanctuary of water and rock offered solace to those seeking respite from the world's chaos.",
    "As twilight blanketed the city, streetlights flickered to life, casting a soft glow on the urban landscape. The hum of distant traffic blended with the laughter of people strolling through the streets. Skyscrapers loomed above, their shimmering windows reflecting the city's vibrant energy. Sidewalks pulsed with the rhythm of footsteps, creating a symphony of movement. Amidst the bustling metropolis, hidden pockets of tranquility beckoned, offering a moment of calm amidst the urban chaos.",
    "At the edge of the horizon, the sun dipped below the ocean's embrace, painting the sky in hues of gold and pink. Waves gently lapped against the sandy shore, leaving delicate traces of foam in their wake. Seagulls glided effortlessly on the sea breeze, their cries echoing across the vast expanse. The salty scent mingled with the tang of seaweed, carrying the promise of adventure and endless possibilities. In this coastal dreamscape, the boundary between land and sea blurred into a symphony of elements.",
    "In the heart of a bustling market, vibrant colors filled the air, tempting the senses. Fragrant spices wafted from open stalls, intermingling with the aroma of freshly baked bread. Shouts and laughter echoed through the narrow alleyways, creating a lively cacophony. Vendors passionately extolled the virtues of their wares, beckoning customers with persuasive words. Among the crowd, curious eyes roamed, eager to explore the treasures hidden within the market's labyrinthine embrace.",
    "A gentle breeze swept across the open meadow, causing the tall grass to sway in rhythm. The sky stretched infinitely above, a vast canvas painted with wisps of clouds. Bees buzzed lazily from flower to flower, while butterflies fluttered on delicate wings. The earthy fragrance of soil mingled with the sweet scent of wildflowers, creating a symphony of smells. In this idyllic setting, time seemed suspended, inviting one to revel in the simplicity of nature's embrace.",
    "In a realm of mystic allure, ancient runes glowed with arcane power. Shadows danced upon mossy stones, as whispers of enchantment filled the air. Creatures unseen rustled in the underbrush, their presence felt but never seen. Crystal-clear waters cascaded over smooth rocks, forming a celestial symphony. Sunbeams pierced the dense foliage, illuminating emerald ferns and blooming petals. Here, time wove a tapestry of ethereal beauty, where dreams took flight on wings of imagination. Step into this realm, where magic and wonder coexist in perfect harmony.",
    "In the quiet solitude of the desert, dunes stretched as far as the eye could see. The sun blazed overhead, casting a golden glow upon the arid landscape. Cacti stood tall and proud, their spines glistening with the morning dew. A gentle wind whispered ancient tales, carrying grains of sand on its playful dance. The desert, seemingly barren, held secrets in its vast expanse, awaiting intrepid adventurers to uncover its mysteries.",
    "In the embrace of a winter wonderland, snowflakes drifted lazily from the heavens, blanketing the earth in a pristine white. The air was crisp and still, carrying the promise of a quiet serenity. Frost adorned branches, turning them into intricate sculptures. Footsteps created a soft crunch as they traversed the snowy terrain. Nature stood frozen in time, offering a breathtaking spectacle of icy beauty. Here, in the hushed landscape, one could find solace and marvel at the enchantment of winter's embrace.",
    "Beneath a star-studded sky, a campfire crackled and cast a warm glow upon the faces of friends gathered around. Tales of adventure and laughter filled the air, intermingling with the scent of toasted marshmallows. Shadows danced on the forest floor as night creatures serenaded the night. Under the canopy of trees, a sense of camaraderie and belonging blossomed. In this shared moment of connection, time seemed to slow, allowing hearts and minds to be nourished by the magic of friendship and the flickering flames."]
var ind = Math.round(Math.random() * 10)
var para =  paragraphs[ind]
var cont = document.getElementById("cont")
console.log(Math.round(para.length/4.7))
cont.innerHTML = para;
let count = 0
let correct = 0
let stroke = 0
let time = 59
function timer(){
    let myinterval = setInterval(function(){
        var timer = document.getElementById("timer")
        document.getElementById("WPM").innerHTML = Math.round(((correct/4.7)/(60 -time))*60) + " WPM"
        document.getElementById("acc").innerHTML = "Accuracy: " + Math.round((correct/stroke)*1000)/10 + "%"
        if(time <= 10){
            timer.innerHTML = "Time " + '<span style="color:red">' + "0:" + ((time - time %10)/10) + time%10 + '</span>'
        }
        else{
            timer.innerHTML = "Time 0:" + ((time - time %10)/10) + time%10
        }
        if(time <= 0 || count == para.length){
            clearInterval(myinterval)
            time = -1
        }
        time -= 1
    }, 1000)
}
let timec = 0
window.addEventListener("keydown", function(event){
    
    if(time >= 0 && event.key != "Shift"){
    if(timec == 0){
        timer()
        timec = 1
    }
    eventee(event)}
})

function eventee(event){
    var eve = event.key
    console.log(eve)
    var res = ""
    if(eve=="Backspace"){
        count -= 1
    }
    else{stroke += 1}
    for(i=count; i<para.length; i++){
        if(i==count && eve != "Backspace"){ 
            let val = para[i]
            if(para[i] == " "){val = "_"}
            if (eve === para[i])   
            {res += '<span id="rig">' + para[i] + '</span>';
            correct += 1}
            
            else{
                res += '<span id="wro">' + val + '</span>';
            }
        }
        else{
            res+= para[i]
        }
    }
    cont.innerHTML =  cont.innerHTML.substring(0, count*23) + res;
    if(eve!="Backspace")
        {count += 1}
}