def binSe(kumpulan, terget):
    #mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1

    #secara berulang belah runtutan itu menjadi separuhnya
    #   sampai targetnya ditemukan
    while low <= high:
            #temukan pertengahan runtut itu
        mid = (high + low) // 2
            #Apakah pertengahanya semua target?
        if kumpulan[mid] == target:
            return True
            #ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid - 1
            #atau targetnya ada di sebelah kananya?
        else:
            low = mid + 1
        #jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False
