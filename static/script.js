document.addEventListener('DOMContentLoaded', () => {
    const carrito = document.querySelector('#carrito');
    const listaCarrito = document.querySelector('#lista-carrito tbody');
    const vaciarCarritoBtn = document.querySelector('#vaciar-carrito');
    const totalCarritoElement = document.querySelector('#total-carrito');

    const productosGrid = document.querySelector('.producto-cuerpo'); 

    let articulosCarrito = [];

    cargarCarritoDesdeLocalStorage();
    calcularTotal();

    if (productosGrid) {
        productosGrid.addEventListener('click', agregarProducto);
    }
    
    vaciarCarritoBtn.addEventListener('click', vaciarCarrito);
    carrito.addEventListener('click', eliminarProducto);

    function agregarProducto(e) {

        if (e.target.classList.contains('agregar-carrito')) {
            e.preventDefault(); 
            const productoSeleccionado = e.target.closest('.producto');
            leerDatosProducto(productoSeleccionado);
            mostrarMensaje('Producto añadido al carrito', 'success');
        }
    }

    function eliminarProducto(e) {
        e.preventDefault();
        if (e.target.classList.contains('borrar-producto')) {
            const productoId = e.target.getAttribute('data-id');

            articulosCarrito = articulosCarrito.map(producto => {
                if (producto.id === productoId) {
                    producto.cantidad--;
                    if (producto.cantidad === 0) {
                        return null;
                    }
                }
                return producto;
            }).filter(producto => producto !== null);

            carritoHTML();
            guardarCarritoEnLocalStorage();
            calcularTotal();
            mostrarMensaje('Producto eliminado/cantidad reducida', 'info');
        }
    }

    function leerDatosProducto(producto) {
        const infoProducto = {
            imagen: producto.querySelector('img').src,
            titulo: producto.querySelector('h3').textContent,
            precio: parseFloat(producto.querySelector('.precio').textContent.replace('$', '')),
            id: producto.querySelector('.agregar-carrito').getAttribute('data-id'),
            cantidad: 1
        };

        const existe = articulosCarrito.some(producto => producto.id === infoProducto.id);
        if (existe) {
            articulosCarrito = articulosCarrito.map(producto => {
                if (producto.id === infoProducto.id) {
                    producto.cantidad++;
                    return producto;
                } else {
                    return producto;
                }
            });
        } else {
            articulosCarrito.push(infoProducto);
        }
        carritoHTML();
        guardarCarritoEnLocalStorage();
        calcularTotal();
    }

    function carritoHTML() {
        limpiarHTML();

        if (articulosCarrito.length === 0) {
            listaCarrito.innerHTML = '<tr><td colspan="5">El carrito está vacío</td></tr>';
            return;
        }

        articulosCarrito.forEach(producto => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><img src="${producto.imagen}" width="50"></td>
                <td>${producto.titulo}</td>
                <td>$${producto.precio.toFixed(2)}</td>
                <td>${producto.cantidad}</td>
                <td><a href="#" class="borrar-producto" data-id="${producto.id}">X</a></td>
            `;
            listaCarrito.appendChild(row);
        });
    }

    function limpiarHTML() {
        while (listaCarrito.firstChild) {
            listaCarrito.removeChild(listaCarrito.firstChild);
        }
    }

    function vaciarCarrito() {
        articulosCarrito = [];
        limpiarHTML();
        guardarCarritoEnLocalStorage();
        calcularTotal();
        mostrarMensaje('Carrito vaciado', 'warning');
    }

    function calcularTotal() {
        let total = articulosCarrito.reduce((sum, item) => sum + (item.precio * item.cantidad), 0);
        totalCarritoElement.textContent = `Total: $${total.toFixed(2)}`;
    }

    function guardarCarritoEnLocalStorage() {
        localStorage.setItem('carrito', JSON.stringify(articulosCarrito));
    }

    function cargarCarritoDesdeLocalStorage() {
        const carritoLS = localStorage.getItem('carrito');
        if (carritoLS) {
            articulosCarrito = JSON.parse(carritoLS);
            carritoHTML();
        }
    }

    function mostrarMensaje(mensaje, tipo) {
        const container = document.querySelector('.messages-container');
        if (!container) {
            console.warn('No se encontró el contenedor de mensajes (.messages-container).');
            return;
        }

        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', tipo);
        messageDiv.textContent = mensaje;
        container.appendChild(messageDiv);

        setTimeout(() => {
            messageDiv.remove();
        }, 3000);
    }
});