var user = {
    init: function(){
        $('create_page').addEvent('submit', function(e){
            e.stop();
            user.savePages();
        });
    },
		
	savePages: function(){
        var request = new Request.JSON({
            async: false,
            method: 'post',
            noCache: false,
            onSuccess: function(responseText, responseXML){
            	var newA = new Element("a", {text: responseText.name,
            		href: responseText.url});
            	var newLI = new Element("li");
            	newLI.adopt(newA);
            	$$(".site-list").adopt(newLI); 
            },
            onFailure: function(xhr){
                console.log(xhr);
            },
            url: '/api/page/'
        });

        request.post($('create_page').toQueryString());
	}
};

window.addEvent('domready', function() {
	user.init();
});