<?php
/*
*  GNU General Public License v3.0
*  Contributors: ADD YOUR NAME HERE, Mike P. Sinn
 */

namespace App\Properties\DeviceToken;
use App\Models\DeviceToken;
use App\Traits\PropertyTraits\DeviceTokenProperty;
use App\Properties\Base\BaseUserIdProperty;
use App\Traits\HasUserFilter;
class DeviceTokenUserIdProperty extends BaseUserIdProperty
{
    use DeviceTokenProperty;
    use HasUserFilter;
    public $table = DeviceToken::TABLE;
    public $parentClass = DeviceToken::class;
}
