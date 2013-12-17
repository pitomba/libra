var user = {
    init: function(){
        $('create_page').addEvent('submit', function(e){
            e.stop();
            user.changePages(action="add");
        });

        $$('.btn-remove').addEvent('click', function(e){
            e.stop();
            user.changePages(action="delete");
        });
        
        $$('.logout').addEvent('click', function(e){
        	Cookie.dispose('LIBRAID');
        	FB.logout(function(){
        		window.location.href = '/';
        	});
        });
    },
		
    changePages: function(action){
        var request = new Request.JSON({
            async: false,
            method: 'delete',
            emulation: false,
            noCache: false,
            onSuccess: function(responseText, responseXML){
            	if(action=='add'){
                	var newA = new Element("a", {text: responseText.name,
                		href: responseText.url});
                	var newLI = new Element("li");
                	newLI.adopt(newA);
                	$$(".site-list").adopt(newLI); 
            	}
            	else{
            	}

            },
            onFailure: function(xhr){
                console.log(xhr);
            },
            url: '/api/page/'
        });

        if(action=='add'){
        	request.post($('create_page').toQueryString());
        }
        else{
        	var parent = this.getParent();
        	console.log(parent)
        	request.send($('create_page').toQueryString());
        }
	}
};

window.addEvent('domready', function() {
	user.init();
});