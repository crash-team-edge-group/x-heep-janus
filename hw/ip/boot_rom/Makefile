# See LICENSE.SiFive for license details

boot_rom = boot_rom.sv

GCC?=$(RISCV_XHEEP)/bin/$(COMPILER_PREFIX)elf-gcc
OBJCOPY?=$(RISCV_XHEEP)/bin/$(COMPILER_PREFIX)elf-objcopy
OBJDUMP?=$(RISCV_XHEEP)/bin/$(COMPILER_PREFIX)elf-objdump
PYTHON?=python

INC_FOLDERS                 = $(sort $(dir $(wildcard ../../../sw/device/lib/drivers/*/)))
INC_FOLDERS                += $(sort $(dir $(wildcard ../../../sw/device/lib/base/*/)))
INC_FOLDERS                += $(sort $(dir $(wildcard ../../../sw/device/lib/runtime/)))
INC_FOLDERS_GCC             = $(addprefix -I ,$(INC_FOLDERS))

all: $(boot_rom) boot_rom.dump

%.sv: %.img
	$(PYTHON) gen_rom.py $<

# JANUS: ROM_KB sets the image size limit (default 1 KiB, unchanged); JANUS_BOOT_BIN replaces the
# compiled boot_rom.S by a prebuilt flat binary (janus/sw/boot, linked at the ROM address)
ROM_KB ?= 1

%.img: %.bin
	dd if=$< of=$@ bs=1024 count=$(ROM_KB)

ifneq ($(strip $(JANUS_BOOT_BIN)),)
%.bin: $(JANUS_BOOT_BIN)
	cp $< $@
else
%.bin: %.elf
	$(OBJCOPY) -O binary $< $@
endif

%.elf: $(findstring boot_rom, $(boot_rom)).S link.ld
	$(GCC) $(INC_FOLDERS_GCC) -Tlink.ld $< -nostdlib -fPIC -static -Wl,--no-gc-sections -o $@

%.dump: %.elf
	$(OBJDUMP) -d $< --disassemble-all --disassemble-zeroes --section=.text --section=.text.startup --section=.text.init --section=.data  > $@

clean:
	rm -f *.img *.bin *.sv .*dump
