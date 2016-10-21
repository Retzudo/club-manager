var eventBus = new Vue();

Vue.http.headers.common['X-CSRFToken'] = getCookie('csrftoken');

Vue.component('new-club-modal', {
    data: function () {
        return {
            name: null
        }
    },

    methods: {
        createClub: function (event) {
            var that = this;
            if (this.name) {
                this.$http.post('/api/v1/clubs/', {
                    'name': this.name
                })
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {
                    that.name = null;
                    that.closeModal();
                    eventBus.$emit('new-club', data)
                });
            }
        },

        closeModal: function () {
            $(this.$el).modal('hide');
        }
    }
});

new Vue({
    el: '#account-app',

    data: {
        clubs: [],
        clubToDelete: null,
    },

    created: function () {
        var that = this;
        fetch('/api/v1/clubs/', {
            credentials: 'same-origin'
        }).then(function (response) {
            return response.json()
        }).then(function (clubs) {
            that.clubs = that.clubs.concat(clubs);
        });
        eventBus.$on('new-club', this.addClub);
        eventBus.$on('delete-club', this.deleteClub);
    },

    methods: {
        addClub: function(club) {
            this.clubs.push(club);
        },
        deleteClub: function(id) {
            this.clubs = this.clubs.filter(function (club) {
                return club.id !== id;
            });
            this.clubToDelete = null;
        }
    }
});