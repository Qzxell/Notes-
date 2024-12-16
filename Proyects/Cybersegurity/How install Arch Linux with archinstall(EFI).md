## 1. Conectar a internet
con iwctl
```bash
station wlan0 connet <SSID>
```

## 2. Particionar el disco
con el comando
```bash
cfdisk /dev/sdXXX
```
1g para la EFI y el resto para el sistea

## 3. Formatear las particiones
```linux
mkfs.fat -F32 /dev/EFI
mkfs.ext4 /dev/system
```
## 4. Montar las particiones

```bash
mount /dev/system /mnt
mount --mkdir /dev/EFI /mnt/boot
```
## 5. Install with archinstall
en la part de "dik configuration" use manual partition: /mnt
 y el resto es personalizado.
Al terminar presionar "yes" exit and poweroff


## 6. Dual boot with Windows

```bash
sudo pacman -S os-prober ntfs-3g
```
### 6.1 descomentar la ultima linea de /etc/default/grub
### 6.2 Montar el sistema efi de windows en /boot/EFI
```bash
mount /dev/EFIwin /boot/efi
```

```bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
sudo os-prober
```
con esto finaliza la instalacion y configuracion del grub





