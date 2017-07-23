<html>
	<head>
	Label Data
        </head>
        <body>
        <form action="/label" method='post'>
	<p>True sentence: {{docum}}</p>
	<br>
	False sentence:
	<input type="text" name="input_sentence" value={{docum}} style="width: 500px" />
	<input type="text" name="output_sentence" value={{docum}} hidden/>
	<input type="text" name="id_data" value={{id_text}}  hidden/>
	<br><br>
	<input type="submit" value="Submit" >
	<!--<input onclick="jump()" type="button" value="next">-->
	</form> 
	<!--<script type="text/javascript">
		function jump(){
			window.location.href = '/login';
		}
	</script>-->
        </body>
</html>
