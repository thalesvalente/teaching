<?php
// Obtém o caminho do arquivo atual
$currentPath = basename($_SERVER['PHP_SELF']);

// Define a classe ativa para o item de navegação correspondente
function isActive($page)
{
    global $currentPath;
    if ($currentPath == $page) {
        echo 'active';
    }
}
?>


<!-- Page Wrapper -->
<div id="wrapper">

<!-- Sidebar -->
<ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

    <!-- Sidebar - Brand -->
    <a class="sidebar-brand d-flex align-items-center justify-content-center" href="dashboard.php">
        <div class="sidebar-brand-icon rotate-n-15">
            <i class="fas fa-shopping-basket"></i>
        </div>
        <div class="sidebar-brand-text mx-3">Mercadinho</div>
    </a>

    <!-- Divider -->
    <hr class="sidebar-divider my-0">

    <!-- Divider -->
    <hr class="sidebar-divider">

    <!-- Heading -->
    <div class="sidebar-heading">
        Sunny
    </div>

    <li class="nav-item <?php isActive('dashboard.php'); ?>">
        <a class="nav-link" href="dashboard.php">
            <i class="fas fa-fw fa-chart-area"></i>
            <span>Dashboard</span>
        </a>
    </li>

    <li class="nav-item <?php isActive('stock.php'); ?>">
        <a class="nav-link" href="stock.php">
            <i class="fas fa-box-open"></i>
            <span>Estoque</span>
        </a>
    </li>

    <li class="nav-item <?php isActive('user_admin.php'); isActive('user_funcionario.php');?>">
        <a class="nav-link" href="../api/user/user.php">
            <i class="fas fa-fw fa-user"></i>
            <span>Usuário</span>
        </a>
    </li>


    <!-- Divider -->
    <hr class="sidebar-divider d-none d-md-block">

    <!-- Sidebar Toggler (Sidebar) -->
    <div class="text-center d-none d-md-inline">
        <button class="rounded-circle border-0" id="sidebarToggle"></button>
    </div>

</ul>
<!-- End of Sidebar -->

