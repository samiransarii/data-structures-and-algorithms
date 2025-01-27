func gcdOfStrings(str1 string, str2 string) string {
    // Check if both the strings have non-zero GCD string.
    // Check if they have different orders or the same
    if str1 + str2 != str2 + str1 {
        return ""
    }

    // Calculate the GCD
    gcd := func(a, b int) int {
        for b != 0 {
            a, b = b, a%b
        }

        return a
    }

    // Find the base gcd
    maxLength := gcd(len(str1), len(str2))
    return str1[:maxLength]
}