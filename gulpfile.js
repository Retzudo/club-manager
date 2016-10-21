var gulp = require('gulp');
var rollup = require('gulp-rollup');
var sourcemaps = require('gulp-sourcemaps');
var babelRollup = require('rollup-plugin-babel');

gulp.task('js', function () {
    return gulp
        .src('./static/src/js/main.js')
        .pipe(sourcemaps.init())
        .pipe(rollup({
            entry: './static/src/js/main.js',
            format: 'cjs',
            plugins: [babelRollup()]
        }))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('./static/dist/js/'));
});

gulp.task('default', ['js']);