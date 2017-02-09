#Tyler Moore
#Starter code for HW5 Q1

def read_playlist(filename):
    """
    Input: filename of CSV file listing (song,artist,genre) triples
    Output: List of (song,artist,genre)
    """
    playlist = []
    for line in open(filename):
        bits = [b.strip() for b in line.split(',')]
        playlist.append(bits)
    return playlist

def iter_playlist_transform(s,t,compareType="Song"):
    """
    Computes the edit distance for two playlists s and t, and prints the minimal edits
      required to transform playlist s into playlist t.
    Inputs:
    s: 1st playlist (format: list of (track name, artist, genre) triples)
    t: 2nd playlist (format: list of (track name, artist, genre) triples)
    compareType: String indicating the type of comparison to make.
       "Song" (default): songs in a playlist are considered equivalent if the
         (song name, artist, genre) triples match.
       "Genre": songs in a playlist are considered equivalent if the same genre is used.
       "Artist": songs in a playlist are considered equivalent if the same artist is used.
    Output: The minimum edit distance and the minimal edits required to transform playlist
      s into playlist t.
    """
    C, s, t = []," "+s," "+t
    # for j in range(len(t)):
    #     C[0, j] = j
    # for i in range(1, len(s)):
    #     C[i, 0] = i
    C.append(range(len(t)+1))
    for i in range(len(s)):
        C.append([i+1])
    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if compareType == "Song" and s[i - 1] == t[j - 1]:
                c_match = C[i - 1, j - 1]
            elif compareType == "Genre" and s[i - 1][2] == t[j - 1][2]:
                c_match = C[i - 1, j - 1]
            elif compareType == "Artist" and s[i - 1][1] == t[j - 1][1]:
                c_match = C[i - 1, j - 1]
            else:
                c_match = C[i - 1, j - 1] + 1
            c_ins = C[i, j - 1] + 1
            c_del = C[i - 1, j] + 1
            c_min = min(c_match, c_ins, c_del)
            C[i, j] = c_min
    print C[i, j]
    for a in range(0, len(s)):
        for b in range(0, len(t)):
            print C[a, b]
        print "\n"
    print
    Penis = []

    while (i>0 and j>0):
        if i == 0:
            Penis.append("Delete " + str(s[i]))
            j -= 1
        elif j == 0:
            Penis.append("Insert" + str(t[j]))
            i -= 1
        else:
            if C[i - 1, j - 1] == C[i, j]:
                Penis.append("Keep" + str(s[i]))
                i -= 1
                j -= 1
            else:
                next = min(C[i - 1, j], C[i - 1, j - 1], C[i, j - 1])
                if next == C[i - 1, j - 1]:
                    Penis.append("Replace" + str(s[i]) + " with " + str(t[j]))
                    i -= 1
                    j -= 1
                elif next == C[i - 1, j]:
                    Penis.append("Insert" + str(t[j]))
                    i -= 1
                elif next == C[i, j - 1]:
                    Penis.append("Delete " + str(s[i]))
                    j -= 1
    for g in Penis:
        print g + "/n"


if __name__=="__main__":
    #obtain local copy from http://secon.utulsa.edu/cs2123/blues1.csv
    b1 = read_playlist("blues1.csv.csv")
    #obtain local copy from http://secon.utulsa.edu/cs2123/blues2.csv
    b2 = read_playlist("blues2.csv.csv")
    print "Playlist 1"
    for song in b1:
        print song
    print "Playlist 2"
    for song in b2:
        print song
    print "Comparing playlist similarity by song"
    iter_playlist_transform(b1,b2)
    print "Comparing playlist similarity by genre"
    iter_playlist_transform(b1,b2,"Genre")
    print "Comparing playlist similarity by artist"
    iter_playlist_transform(b1,b2,"Artist")
    #include your own playlists below