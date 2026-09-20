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

# RAIL FENCE KEY = 2

for (int i = 0; i < pt.length(); i++) {
if (i % 2 == 0) {
r1 += pt.charAt(i);
} else {
r2 += pt.charAt(i);
}
}

# RAIL FENCE CUSTOM KEY

char[][] rail = new char[key][pt.length()];
for (char[] row : rail) Arrays.fill(row, '\n');

int r =0 ;
boolean down = true;
for (int i=0 ; i<pt.length() ; i++){
rail[r][i] = pt.charAt(i);

    if (r==0)down = true;
    else if (r == key-1) down = false ;

    r += down ? 1:-1;

}
String cipher ="";
for(char[] row : rail){
for(char c : row){
if ( c != '\n') cipher += c;
}
}

# COLUMNAR

int row = (text.length() + col -1 )/col;
char[][] m = new char[row][col];
int k = 0 ;
for(int i =0; i< row; i++){
for(int j=0 ; j< col ; j++){
if ( k< text.length()){
m[i][j] = text.charAt(k++);
}else{
m[i][j] = 'X';
}
}
}

# RSA

static int gcd(int a, int b) {
while (b != 0) {
int t = a % b;
a = b;
b = t;
}
return a;
}
static int pow(int a , int b , int n){
int r=1;
while (b-- > 0) r = r * a % n;
return r;
}
public static void main(String[] args) {
int p = 3 , q = 11 , n = p*q;
int phi = (p-1) * (q-1);
int e=2 , d=1;
while (gcd(e,phi) != 1)e++;
while ((e*d) % phi != 1)d++;
int msg =32;
int enc = pow(msg , e , n);
int dec = pow(enc , d , n);

System.out.println("Encrypt : " + enc);
System.out.println("Decrypt : " + dec);
