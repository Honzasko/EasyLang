
print_num:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 64
        mov     QWORD  [rbp-56], rdi
        mov     QWORD  [rbp-48], 0
        mov     QWORD  [rbp-40], 0
        mov     QWORD  [rbp-32], 0
        mov     QWORD  [rbp-24], 0
        mov     QWORD  [rbp-8], 32
        mov     DWORD  [rbp-12], 0
        sub     QWORD  [rbp-8], 1
        lea     rdx, [rbp-48]
        mov     rax, QWORD  [rbp-8]
        add     rax, rdx
        mov     BYTE  [rax], 10
        mov     rax, QWORD  [rbp-56]
        test    rax, rax
        jns     .L3
        mov     DWORD  [rbp-12], 1
        neg     QWORD  [rbp-56]
.L3:
        mov     rcx, QWORD  [rbp-56]
        mov  rdx, -3689348814741910323
        mov     rax, rcx
        mul     rdx
        shr     rdx, 3
        mov     rax, rdx
        sal     rax, 2
        add     rax, rdx
        add     rax, rax
        sub     rcx, rax
        mov     rdx, rcx
        mov     eax, edx
        add     eax, 48
        mov     edx, eax
        sub     QWORD  [rbp-8], 1
        lea     rcx, [rbp-48]
        mov     rax, QWORD  [rbp-8]
        add     rax, rcx
        mov     BYTE  [rax], dl
        mov     rax, QWORD  [rbp-56]
        mov  rdx, -3689348814741910323
        mul     rdx
        mov     rax, rdx
        shr     rax, 3
        mov     QWORD [rbp-56], rax
        cmp     QWORD  [rbp-56], 0
        jne     .L3
        cmp     DWORD  [rbp-12], 0
        je      .L4
        sub     QWORD  [rbp-8], 1
        lea     rdx, [rbp-48]
        mov     rax, QWORD  [rbp-8]
        add     rax, rdx
        mov     BYTE  [rax], 45
.L4:
        mov     eax, 32
        sub     rax, QWORD  [rbp-8]
        mov     rdx, rax
        mov     rax, QWORD  [rbp-8]
        lea     rcx, [rbp-48]
        add     rax, rcx
        mov     rsi, rax
        mov     edi, 1
        mov rax,1
        syscall
        nop
        leave
        ret