const playlist = [
    {title: 'Smells Like Teen Spirit', duration: 301},
    {title: 'Come As You Are', duration: 218},
    {title: 'Something In The Way', duration: 232},
    {title: 'Heart-Shaped Box', duration: 281},
    {title: 'Lithium', duration: 257}
];
  
const totalSeconds = playlist.reduce((total, playlist) => total + playlist.duration, 0);
const totalMinutes = Math.floor(totalSeconds / 60);
const remainingSeconds = totalSeconds % 60;
const playlistCount = playlist.length;

console.log("Playlist:");
playlist.forEach((song, index) => {
  console.log(`${index + 1}. ${song.title} (${song.duration} segundos)`);
})

console.log(`A playlist possui ${playlistCount} músicas e o tempo total de reprodução é de ${totalMinutes} minutos e ${remainingSeconds} segundos.`);
