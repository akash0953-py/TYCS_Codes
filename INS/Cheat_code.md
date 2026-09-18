# Ceasar Cipher

// Encryption
for (int i = 0; i < s.length(); i++) {
char c = s.charAt(i);
if (Character.isUpperCase(c))
enc += (char) ((c - 'A' + k) % 26 + 'A');
else
enc += (char) ((c - 'a' + k) % 26 + 'a');
}

// Decryption of encrypted string
for (int i = 0; i < enc.length(); i++) {
char c = enc.charAt(i);
if (Character.isUpperCase(c))
dec += (char) ((c - 'A' - k + 26) % 26 + 'A');
else
dec += (char) ((c - 'a' - k + 26) % 26 + 'a');
}

# Mono

for (int i = 0; i < pt.length(); i++) {
enc += key.charAt(pt.charAt(i) - 'A');
}
for (int i = 0; i < enc.length(); i++) {
dec += (char) (key.indexOf(enc.charAt(i)) + 'A');
}

# Vernam Cipher

if (pt.length() != key.length()) {
System.err.println("String and key must be same length");
}

String enc = "", dec = "";
for (int i = 0; i < pt.length(); i++) {
enc += (char) ((pt.charAt(i) ^ key.charAt(i)) + 97);
}

for (int i = 0; i < enc.length(); i++) {
dec += (char) ((enc.charAt(i) - 97) ^ key.charAt(i));
}

#
