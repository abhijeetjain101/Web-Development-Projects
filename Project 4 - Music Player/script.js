const musicContainer = document.querySelector('.music-container')
const playBtn = document.querySelector('#play')
const prevBtn = document.querySelector('#prev')
const nextBtn = document.querySelector('#next')
const audio = document.querySelector('#audio')
const progress = document.querySelector('.progress')
// const progressContainer = document.querySelector('.progress-container')
const seek_slider = document.querySelector('.seek_slider')
const title = document.querySelector('#title')
const cover = document.querySelector('#cover')
// const volumeBtn = document.querySelector('.volume')
const volumeUpBtn = document.querySelector('#volume-up')
const volumeDownBtn = document.querySelector('#volume-down')
let volume_slider = document.querySelector(".volume_slider")
let curr_time = document.querySelector(".current-time");
let total_duration = document.querySelector(".total-time"); 


// Song titles
const songs = ['hey', 'summer', 'ukulele']

// Keep track of songs
let songIndex = 2

// Initially load song info DOM
loadSong(songs[songIndex])

// Update song details
function loadSong(song) {
    title.innerText = song
    audio.src = `music/${song}.mp3`
    cover.src = `img/${song}.jpg`
}
// // seek slider
function seekto() {
    seekto = audio.duration*(seek_slider.value/100)
    audio.currentTime = seekto;
}

//function for play and pause
function playSong() {
    musicContainer.classList.add('play')
    playBtn.querySelector('i.fas').classList.remove('fa-play')
    playBtn.querySelector('i.fas').classList.add('fa-pause')

    audio.play()
}

function pauseSong() {
    musicContainer.classList.remove('play')
    playBtn.querySelector('i.fas').classList.add('fa-play')
    playBtn.querySelector('i.fas').classList.remove('fa-pause')

    audio.pause()
}
// Event Listeners to play and pause
playBtn.addEventListener('click', () => {
    const isPlaying = musicContainer.classList.contains('play')

    if(isPlaying) {
        pauseSong()
    } 
    else {
        playSong()
    }
})

//function for prev and nxt
function prevSong() {
    songIndex--

    if(songIndex < 0) {
        songIndex = songs.length - 1
    }

    loadSong(songs[songIndex])
    
    playSong()
}

function nextSong() {
    songIndex++

    if(songIndex > songs.length - 1) {
        songIndex = 0
    }

    loadSong(songs[songIndex])
    
    playSong()
}

// Change song events
prevBtn.addEventListener('click', prevSong)
nextBtn.addEventListener('click', nextSong)

audio.addEventListener('timeupdate', updateProgress)

seek_slider.addEventListener('click', setProgress)

audio.addEventListener('ended', nextSong)


//function to control seek slider progress
function updateProgress(e) {
    const {duration, currentTime} = e.srcElement
    const progressPercent = (currentTime / duration) * 100
    seek_slider.style.width = `${progressPercent}%`
}

function setProgress(e) {
    const width = this.clientWidth
    const clickX = e.offsetX
    const duration = audio.duration

    audio.currentTime = (clickX / width) * duration
}

// volume up, down and mute
function muteSong() {
    document.getElementById('volume-down').add('#volume-mute')
    // document.getElementById.add('volume-down')
    volumeDownBtn.querySelector('i.fas').classList.remove('fa-volume-down')
    volumeDownBtn.querySelector('i.fas').classList.add('fa-volume-mute')

    audio.muted = true;
}


// function unmuteSong() {
//     volumeDownBtn.remove('#volume-mute')
//     volumeDownBtn.add('#volume-down')
//     // document.getElementById.remove('volume-down').add('volume-mute')
//     volumeDownBtn.querySelector('i.fas').classList.add('fa-volume-down')
//     volumeDownBtn.querySelector('i.fas').classList.remove('fa-volume-mute')

//     audio.muted = false;
// }


//Volume Slider Control Function
function setVolume() {
    audio.volume = volume_slider.value/100;
}

// //Event Listeners to control volume-down and mute
// volumeDownBtn.addEventListener('click', () => {
//     const isMute = document.getElementById('volume-down')

//     if(isMute) {
//         unmuteSong()
//     } 
//     else {
//         muteSong()
//     }
// })










// volume.addEventListener('click', () => {
//     const isVolume = navigation.classList.contains('fas fa-volume-up')
// } )