def ma_hoa_ceasar(van_ban, k):
    ket_qua = ""
    for ky_tu in van_ban:
        if ky_tu.isalpha():
            ma_ascii = ord('A') if ky_tu.isupper() else ord('a')
            ky_tu_moi = chr((ord(ky_tu) - ma_ascii + k) % 26 + ma_ascii)
            ket_qua += ky_tu_moi
        else:
            ket_qua += ky_tu  
    return ket_qua


van_ban_goc = "NguyenTranMinhTrang" 
k = 39
ma_hoa = ma_hoa_ceasar(van_ban_goc, k)

print("Văn bản gốc:", van_ban_goc)
print("Văn bản mã hóa:", ma_hoa)
