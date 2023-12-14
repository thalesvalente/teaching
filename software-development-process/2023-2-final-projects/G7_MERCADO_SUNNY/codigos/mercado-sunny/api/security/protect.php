<?php

if (!isset($_SESSION)) {
    session_start();
} 

if (!isset($_SESSION['id'])) {
    header("Location: 404.php");
}
