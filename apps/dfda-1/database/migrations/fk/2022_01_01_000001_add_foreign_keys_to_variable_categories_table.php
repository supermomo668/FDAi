<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class AddForeignKeysToVariableCategoriesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('variable_categories', function (Blueprint $table) {
            $table->foreign(['default_unit_id'], 'variable_categories_default_unit_id_fk')->references(['id'])->deferrable()->on('units');
            $table->foreign(['wp_post_id'], 'variable_categories_wp_posts_ID_fk')->references(['ID'])->deferrable()->on('wp_posts');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::table('variable_categories', function (Blueprint $table) {
            $table->dropForeign('variable_categories_default_unit_id_fk');
            $table->dropForeign('variable_categories_wp_posts_ID_fk');
        });
    }
}
