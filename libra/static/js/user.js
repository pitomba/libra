var user = {
    init: function(){
        $('create_page').addEvent('submit', function(e){
            e.stop();
            user.savePages();
        });
    },
		
	savePages: function(){
        var request = new Request({
            async: false,
            method: 'post',
            noCache: false,
            onSuccess: function(responseText, responseXML){
                console.log(responseText, responseXML);
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