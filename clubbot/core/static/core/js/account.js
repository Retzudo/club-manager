var eventBus = new Vue();

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
                fetch('/api/v1/clubs/', {
                    method: 'POST',
                    credentials: 'same-origin',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({
                        'name': this.name
                    })
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

Vue.component('delete-club-modal', {
    props: ['club'],

    methods: {
        deleteClub: function () {
            var that = this;
            fetch('/api/v1/clubs/' + that.club.id + '/', {
                method: 'DELETE',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            }).then(function (response) {
                if (response.ok) {
                    $(that.$el).modal('hide');
                    eventBus.$emit('delete-club', that.club.id);
                }
            });
        }
    },

    computed: {
        name: function () {
            return this.club ? this.club.name : '';
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