SELECT tr.trackid, tr.name, alb.title, art.name FROM artists  as art
LEFT JOIN albums as alb ON art.artistid = alb.artistid
LEFT JOIN tracks as tr ON alb.albumid = tr.albumid