# Caesar Cipher

## Introduction

The Caesar Cipher is a substitution cipher. It encrypts a message by shifting all it's characters using a given value known as the key. For example encrypting *ABC* to caesar cipher using *2* as the key would be *CDE*.

## About this implementation

This code encrypt/decrypt strings using caesar cipher. It can encrypt any string with chracters in range *32* (*SPACE*)
to *126* (*~*) in ascii code. That is every printable ASCII character. If a character is beyond that range, it keep it
untouched.

### Supported Characters

<pre>
SPACE ! " # $ % & ' ( ) * +  - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~
</pre>

### Complexity

+ Space Complexity: *O(1)*.
+ Encryption Time Complexity: *O(n)*, which *n* is the input string length. 
+ Brute-force Decryption Time Complexity: *O(m.n)*, which *n* is the input string length and *m* is number of possible values for the key (*94* in this case).

## Usage

### Encryption using a specific key

<pre>
./caesar_cipher.py "sample text" -k 8
</pre>

<pre>
>> {iuxtm(|m!|
</pre>

### Decryption using a specific key

<pre>
./caesar_cipher.py '{iuxtm(|m!|' -k -8
</pre>

<pre>
>> sample text
</pre>

### Brute-force Decryption

<pre>
./caesar_cipher.py '{iuxtm(|m!|' -f | head -n 10
</pre>

<pre>
>> key #1: zhtwsl'{l {
key #2: ygsvrk&zk~z
key #3: xfruqj%yj}y
key #4: weqtpi$xi|x
key #5: vdpsoh#wh{w
key #6: ucorng"vgzv
key #7: tbnqmf!ufyu
key #8: sample text
key #9: r`lokd~sdws
key #10: q_knjc}rcvr
</pre>

### Running tests

<pre>
python3 -m unittest -v
</pre>
