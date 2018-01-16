<?php
$arquivo_semente = fopen(__DIR__ . '/semente.txt', 'r');
$arquivo_amostra = fopen(__DIR__ . '/amostra.txt', 'w+r');
 
$matricula = 27;

if ($arquivo_semente)
{
	while(($linha = fgets($arquivo_semente)) !== false)
	{
		fwrite($arquivo_amostra, $linha + $matricula);
		fwrite($arquivo_amostra, PHP_EOL);
	}
	fclose($arquivo_semente);
	fclose($arquivo_amostra);
}
?>