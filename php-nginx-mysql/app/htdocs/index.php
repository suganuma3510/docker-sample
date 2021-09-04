<?php
$dsn      = 'mysql:host=db;dbname=php_sample;';
$user     = 'root';
$password = 'password';

try {
  $db = new PDO($dsn, $user, $password);
  echo 'Hello PHP';
} catch (PDOException $e) {
  echo 'DB接続失敗' . $e->getMessage();
}
