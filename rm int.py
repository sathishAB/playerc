class hi:
    def roman_to_int(self, s):
        rom_val = {'x'=10,'I'=1,'M'=1000}
        int_val = 0
        for i in range(len(s)):
            if (i > 0) and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return (int_val)
print(hi().roman_to_int('XI'))
print(hi().roman_to_int('XX'))
print(hi().roman_to_int('M'))
