	$(document).ready(function(){
		var mappedItems = $('li').map(function (index){
			var replacement = $('<li>').text($(this).text()).get(0);
			if(index == 0){
				$(replacement).text($(replacement).text().toUpperCase());
			}else if(index == 1 || index == 3){
				replacement = null;
			}else if (index == 2){
				replacement = [replacement, $('<li>').get(0)];
				$(replacement[0]).append('<b>-A</b>');
				$(replacement[1]).append('Extra <b>-B</b>');
			}
			return replacement
		});
		$('#results').append(mappedItems);

	});