<?php
/*
*  GNU General Public License v3.0
*  Contributors: ADD YOUR NAME HERE, Mike P. Sinn
 */

namespace App\Properties\MeasurementImport;
use App\Models\MeasurementImport;
use App\Traits\PropertyTraits\MeasurementImportProperty;
use App\Properties\Base\BaseClientIdProperty;
class MeasurementImportClientIdProperty extends BaseClientIdProperty
{
    use MeasurementImportProperty;
    public $table = MeasurementImport::TABLE;
    public $parentClass = MeasurementImport::class;
}