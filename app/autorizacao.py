permissoes_por_papel = {
    "admin": ["cadastro", "editar"],
    "usuario": ["cadastro"]
}

def verificar_rbac(usuario, recurso):
    papel = usuario.get("papel")
    return recurso["recurso"] in permissoes_por_papel.get(papel, [])

def verificar_abac(usuario):
    return usuario.get("idade", 0) >= 18

def verificar_acesso(usuario, recurso):
    return verificar_rbac(usuario, recurso) and verificar_abac(usuario)
