Vue.http.headers.common['X-CSRFToken'] = getCookie('csrftoken');
Vue.http.options.emulateJSON = true;



Vue.component('delete-club-modal', {
    props: ['clubId'],

    methods: {
        deleteClub: function () {
            var that = this;
            this.$http.delete('/api/v1/clubs/' + that.clubId + '/')
            .then(function (response) {
                $(that.$el).modal('hide');
                if (response.ok && response.status === 204) {
                    window.location = '/account';
                }
            });
        }
    }
});

Vue.component('slug-changer', {
    props: ['club'],
    data: function () {
        return {
            errors: {
                slug: []
            }
        };
    },
    methods: {
        change: function () {
            var that = this;
            var body = {
                slug: this.club.slug
            };
            this.$http.patch('/api/v1/clubs/' + this.club.id + '/', body)
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                that.errors = [];
                that.club = data;
                window.location = '/clubs/' + data.slug + '/settings';
            })
            .catch(function (error) {
                return error.json();
            }).then(function (data) {
                that.errors = data;
            });
        }
    }
});

Vue.component('club-settings', {
    props: ['clubId'],
    data: function () {
        return {
            club: null
        };
    },
    mounted: function () {
        var that = this;
        this.$http.get('/api/v1/clubs/' + this.clubId)
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                that.club = data;
            });
    }
});

new Vue({
    el: '#settings',
});